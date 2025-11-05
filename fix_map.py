import re

# Read the source SVG
with open('src/lib/karta_kontur.svg', 'r') as f:
    svg_content = f.read()

# Clean up SVG content
svg_content = re.sub(r'<\?xml[^>]*\?>', '', svg_content)
svg_content = re.sub(r'<!--.*?-->', '', svg_content, flags=re.DOTALL)
svg_content = svg_content.strip()

# Extract svg tag and its content
svg_match = re.search(r'<svg([^>]*)>(.*)<\/svg>', svg_content, re.DOTALL)
if not svg_match:
    raise Exception("Could not find svg tag in karta_kontur.svg")

svg_attrs = svg_match.group(1)
svg_inner_content = svg_match.group(2)

def process_path(match):
    path_attrs_str = match.group(1)
    attrs = dict(re.findall(r'([a-zA-Z\-:]+)="([^"]+)"', path_attrs_str))

    path_id = attrs.get('id')
    if not path_id:
        return match.group(0)

    original_style = attrs.get('style', '')
    style_parts = [part.strip() for part in original_style.split(';') if 'fill:' not in part and 'stroke:' not in part]

    svelte_fill = f"fill:{{$territories['{path_id}'] ? $territories['{path_id}'].owner.color : '#ffffff'}}"
    style_parts.insert(0, svelte_fill)

    attrs['style'] = ';'.join(filter(None, style_parts))

    attrs['on:click'] = f"{{() => handlePathClick('{path_id}')}}"
    attrs['on:keydown'] = f"{{(event) => {{ if (event.key === 'Enter' || event.key === ' ') handlePathClick('{path_id}'); }}}}"
    attrs['class:selected'] = f"{{$selected_territory === '{path_id}'}}"
    attrs['role'] = "button"
    attrs['tabindex'] = "0"

    new_attrs_str = ' '.join([f'{key}="{value}"' for key, value in attrs.items()])

    return f'<path {new_attrs_str} />'

modified_svg_inner = re.sub(r'<path([^>]*)\/?>', process_path, svg_inner_content, flags=re.IGNORECASE | re.DOTALL)

new_script_block = """<script>
    import { territories, selected_territory } from '../../lib/store.js';

    function handlePathClick(pathId) {
        if ($selected_territory === pathId) {
            selected_territory.set(null);
        } else {
            selected_territory.set(pathId);
        }
    }
</script>"""

# Reconstruct the Svelte file
new_content = f"""{new_script_block}

<svg{svg_attrs}>
    {modified_svg_inner}
</svg>

<style>
    path {{
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }}
    path:hover {{
        filter: brightness(0.9);
    }}
    path.selected {{
        stroke: yellow !important;
        stroke-width: 3px !important;
        stroke-opacity: 1 !important;
        filter: brightness(1.1);
    }}
</style>
"""

with open('src/components/game/Map.svelte', 'w') as f:
    f.write(new_content)

print("Map.svelte has been updated.")
