import { createHash } from 'node:crypto';

// 为正文顶层块级元素（段落/引用/列表）生成稳定 id，
// 便于分享指向具体段落的锚点链接（如 #s-1a2b3c4d）。
// id 取内容文本的 sha1 前 8 位，内容不变则 id 不变。
const SECTION_TAGS = new Set(['p', 'blockquote', 'ul', 'ol']);

function textContent(node) {
  if (node.type === 'text') return node.value;
  if (!node.children) return '';
  return node.children.map(textContent).join('');
}

export default function rehypeSectionIds() {
  return (tree) => {
    const used = new Set();
    for (const node of tree.children || []) {
      if (node.type !== 'element' || !SECTION_TAGS.has(node.tagName)) continue;
      if (node.properties?.id) continue;
      const text = textContent(node).trim();
      if (!text) continue;
      const base = 's-' + createHash('sha1').update(text).digest('hex').slice(0, 8);
      let id = base;
      let n = 2;
      while (used.has(id)) id = `${base}-${n++}`;
      used.add(id);
      node.properties = node.properties || {};
      node.properties.id = id;
    }
  };
}
