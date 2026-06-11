import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.string(),
    country: z.string(),
    tags: z.array(z.string()),
    coverImage: z.string(),
    excerpt: z.string(),
    mapCenter: z.tuple([z.number(), z.number()]).optional(),
    mapZoom: z.number().optional(),
    mapPoints: z.array(z.object({
      lat: z.number(),
      lng: z.number(),
      label: z.string().optional(),
    })).optional(),
    gallery: z.array(z.object({
      src: z.string(),
      alt: z.string(),
      caption: z.string().optional(),
    })).optional(),
  }),
});

export const collections = { blog };
