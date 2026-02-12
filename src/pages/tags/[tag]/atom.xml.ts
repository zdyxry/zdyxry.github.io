import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { experimental_AstroContainer as AstroContainer } from 'astro/container';
import { loadRenderers } from 'astro:container';
import { getContainerRenderer } from '@astrojs/mdx';
import { render } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('posts', ({ data }) => !data.draft);
  const tags = new Set<string>();
  
  for (const post of posts) {
    for (const tag of post.data.tags) {
      tags.add(tag);
    }
  }
  
  return Array.from(tags).map(tag => ({
    params: { tag },
  }));
}

export async function GET(context: APIContext) {
  const { tag } = context.params;
  
  const posts = await getCollection('posts', ({ data }) => 
    !data.draft && data.tags.includes(tag as string)
  );
  const sortedPosts = posts
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf())
    .slice(0, 20);

  const container = await AstroContainer.create({
    renderers: await loadRenderers([getContainerRenderer()]),
  });

  const items = await Promise.all(
    sortedPosts.map(async (post) => {
      const { Content } = await render(post);
      const content = await container.renderToString(Content);
      
      const date = new Date(post.data.pubDate);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      const slugPart = post.data.slug || post.slug;
      
      return {
        title: post.data.title,
        description: post.data.description || '',
        pubDate: post.data.pubDate,
        link: `/${year}/${month}/${day}/${slugPart}/`,
        categories: post.data.tags,
        content: content,
      };
    })
  );

  return rss({
    title: `标签: ${tag} - Yiran's Blog`,
    description: `标签 "${tag}" 的最新文章`,
    site: context.site?.toString() || 'https://zdyxry.github.io',
    items,
    customData: `<language>zh-CN</language>`,
  });
}
