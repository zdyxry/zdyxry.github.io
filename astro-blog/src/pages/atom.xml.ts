import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { experimental_AstroContainer as AstroContainer } from 'astro/container';
import { loadRenderers } from 'astro:container';
import { getContainerRenderer } from '@astrojs/mdx';
import { render } from 'astro:content';

export async function GET(context: APIContext) {
  const posts = await getCollection('posts', ({ data }) => !data.draft);
  const sortedPosts = posts
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf())
    .slice(0, 20);  // 只保留最近 20 篇文章

  // 初始化 Astro 容器用于渲染 MDX
  const container = await AstroContainer.create({
    renderers: await loadRenderers([getContainerRenderer()]),
  });

  const items = await Promise.all(
    sortedPosts.map(async (post) => {
      const { Content } = await render(post);
      // 渲染内容为 HTML 字符串
      const content = await container.renderToString(Content);
      
      // Generate Hugo-style URL
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
    title: 'My Blog',
    description: '记录生活，分享技术，探索世界',
    site: context.site?.toString() || 'https://zdyxry.github.io',
    items,
    customData: `<language>zh-CN</language>`,
  });
}
