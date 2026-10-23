# Danish blog integration

Prepared locally on `conservative-homepage-and-blog`; nothing has been pushed or deployed.

The English navigation says **Blog**. Its Danish landing page is **Tanker**.
All five posts retain their titles, original publication timestamps, tags, author,
and complete bodies. The index descriptions are new, informal summaries.
Malformed `tab:https://` links are repaired and the Mahler image is copied into
`images/blog/` to avoid collisions. English academic news remains in `_posts`;
the personal posts live separately in `_blog`.

The homepage implements the selected conservative evolution: profile sidebar,
short introduction, book feature, five selected publications, and cases.
The Danish blog is accessible through the menu only, with no homepage feature.
The previous complete biography is preserved
at `/biography/`. The Book page contains the supplied synopsis and credits Oxford University Press
as the forthcoming publisher; the homepage book feature matches. The Cases page includes
the MobilePay teaching case (8 October 2026) and the forthcoming series
"On the shoulder of giants: The origins of the Danish life science industry". Existing publication and CV pages
keep their familiar layouts.

## Publication sequence

1. Build this branch with `bundle install` and `bundle exec jekyll build`.
2. Review `/blog/`, all five full articles, the Mahler image, and the homepage.
3. Publish the academic-site changes and verify the new URLs publicly.
4. Only then publish the blog repository's `prepare-blog-redirects` branch.
   Keep `blog.msdahl.net` configured on its existing GitHub Pages project.

The old Hugo project uses static HTML redirects, with canonical tags and fallback
links. These are browser redirects, not HTTP 301 responses. Its homepage,
post archive, about page, and taxonomy pages lead to the new blog index; each
article leads to the matching migrated article. Existing filename slugs are
retained even when their year differs from the original publication date.

The old repository remains available as an archive. Existing email-to-post
automation will need to be changed separately before it is used to publish new
posts: it currently writes to the Hugo project.

## Post destinations

The existing `/posts/<filename>/` URLs at `blog.msdahl.net` redirect to
`https://msdahl.net/blog/<filename>/`:

- `2025-04-23-aabs-strategi-og-genrejsning-om-at-bevare-ilden-fremfor-at-tilbede-asken-aab-sport-strategi`
- `2025-04-20-forbandelsens-mesterskab-aab-sport-strategi`
- `2015-08-15-hvem-ansaettes-i-nye-virksomheder-forskning`
- `2015-08-04-om-geografisk-mobilitet-pa-det-danske-arbejdsmarked-forskning-mobilitet`
- `2015-08-04-om-organisatoriske-forandringer-forskning-ledelse-stress`

## Validation completed

The full academic site and old-blog redirect project both built successfully.
Generated-output checks confirmed all five article pages, matching old-domain
redirect destinations, Danish date labels, navigation targets, and the copied
image. Article bodies and original metadata were compared with the source
repository; only malformed link prefixes and the image path were changed.
The Jekyll build reports existing theme deprecation warnings. Browser-based
visual checks remain to be performed before publication.
