Full article: https://blog.cg-wire.com/kitsu-cli

## Usage

1. Create a local Kitsu instance with [`kitsu-docker`](https://github.com/cgwire/kitsu-docker) and setup a production
2. Create a single executable binary: `python3 -m PyInstaller --onefile --name kitsu-cli cli.py`
3. Run the CLI: `./kitsu-cli production list`
4. Pick a production from your local Kitsu instance

For the render fetcher:

1. In Kitsu, create a new shot and publish a preview file to a Rendering TODO task.
2. Create a single executable binary: `python3 -m PyInstaller --onefile --name kitsu-cli fetch.py`
3. Run the CLI: `./kitsu-cli pull "my prod" .`
4. The CLI will download the .blend preview file
