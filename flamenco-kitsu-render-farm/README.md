Full article: [Flamenco Kitsu Render Farm](https://blog.cg-wire.com/flamenco-kitsu-render-farm)

## Usage

1. Add custom job type to Flamenco /scripts/kitsu-render.js
1. Add Python script to Flamenco Worker /kitsu-render.py
2. Add asset to render in Kitsu (you'll need to create an asset, link it to a shot, and upload a .blend file as a revision for a TODO Rendering task)
3. Launch script to add Kitsu Render job ./launch.sh
4. Check your asset has been rendered and uploaded to Kitsu
