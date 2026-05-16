import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.union([z.string(), z.null()]).optional().transform(val => val || undefined),
    // Support both pubDate and date for backward compatibility
    pubDate: z.coerce.date().optional(),
    date: z.coerce.date().optional(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    tags: z.array(z.string()).optional().default([]),
    draft: z.boolean().default(false),
    // Custom slug for Hugo-style URLs: /YYYY/MM/DD/slug/
    customSlug: z.string().optional(),
    // Explicit slug for Hugo URL compatibility
    slug: z.string().optional(),
  }).transform((data) => {
    // Normalize date fields - use pubDate if available, otherwise use date
    const pubDate = data.pubDate || data.date || new Date();
    
    return {
      ...data,
      pubDate: pubDate,
    };
  }),
});

export const collections = { posts };
