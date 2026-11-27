BITDELTA GLOBAL WEEK — HTML EMAIL PACKAGE
Source: Figma COM-NewsLetter / node 132:26 / BitDelta 27.11.26
https://www.figma.com/design/albp1GgHdDQ3GBzwHatJqg/COM-NewsLetter?node-id=132-26

FILES
newsletter.html — responsive table email, inline presentation CSS and small mobile stylesheet.
preview.html — identical local preview; keep assets beside it.
assets/ — 26 PNG/JPEG assets. Logos, icons and illustrations rasterized from the exact native Figma PDF export at source resolution; background images recovered from the original .fig image data. No substitute artwork.
newsletter.txt — extracted source text for the plain-text version; edit ordering if needed in your campaign editor.
links.json — every source destination with its Figma node/provenance (18 linked elements, 17 unique destinations).
link-checks.json — observed HTTP responses, not a guarantee of destination content.
prepare-email.py — converts local image references to your actual public HTTPS media URLs.
validation.json — structural and browser check results.

CLEVERTAP SETUP
1. Upload assets/ to your approved public HTTPS media host or CleverTap media library.
2. Replace ALL assets/... references in newsletter.html with actual public URLs, including background-image and VML references. A helper is included:
   python3 prepare-email.py --base-url YOUR_ACTUAL_HTTPS_ASSET_DIRECTORY
   Alternatively pass --map urls.json containing {"assets/logo.png":"actual HTTPS URL", ...} for each asset.
3. Paste newsletter-clevertap.html into the custom HTML email editor. Use newsletter.txt for the text alternative. Suggested subject: BitDelta Global Week | 20–26 November 2026.
4. Keep *|UNSUBSCRIBE|* intact. This is the documented CleverTap send-time token, added below the original legal footer. It is not a working local preview URL.
5. Send a test from your CleverTap account to Gmail, Apple Mail and Outlook before launching. Confirm media, tracking, unsubscribing, and your sender configuration.
Official unsubscribe reference: https://docs.clevertap.com/docs/handling-unsubscribes

VALIDATION AND LIMITS
Desktop browser preview checked at 800px viewport with a 600px email. Mobile checked at 375px and 320px; no horizontal overflow; all image elements loaded. The desktop layout and footer were visually inspected. A full-page browser capture had stitching artifacts; DOM inspection confirms one occurrence of each section and 19 total anchors.
Exact source URL strings including UTM tracking were preserved. Seven unique web destinations returned HTTP 200. LinkedIn, CoinGecko and support returned 403; six BitDelta destinations returned 429. These cannot be called verified reachable. The mailto address is preserved; mailbox delivery was not tested. HTTP 200 does not prove campaign availability or that the correct content remains live.

The source is a 1200px-wide desktop design, adapted to a 600px email. Mobile stacks cards, story, listing and post columns, enlarges small card copy, and hides the decorative hero background to protect text contrast. No separate mobile Figma frame was supplied.
Archivo is preferred when installed; Arial/Helvetica are email-safe fallbacks. Poppins and DIN 2014 footer type use the same fallback stack. Line wraps and overall height therefore differ across clients. Live text replaces absolute design positioning. Banner tint/gradient are approximated; PNG artwork includes its source backdrop. Exact pixel parity is not claimed.
The layout uses presentation tables, inline CSS, image alt text, an Outlook fixed-width wrapper and VML for the two lower background banners. The hero falls back to a solid navy background in Outlook. Some clients may strip media queries or restyle dark mode. Gmail/Outlook/Apple Mail inbox testing and CleverTap ingestion were NOT performed; there is no connected sending account or public media host available in this task.
This is a completed local implementation package, not a send-ready campaign until public media URLs are supplied and an inbox test passes. Source financial figures and dates are reproduced as supplied, not independently researched or updated.
