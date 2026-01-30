import gazu

gazu.set_host("http://localhost/api")
user = gazu.log_in("admin@example.com", "mysecretpassword")

projects = gazu.project.all_projects()
project = projects[0]

asset_types = gazu.asset.all_asset_types()
asset_type = asset_types[0]

asset = gazu.asset.new_asset(
    project,
    asset_type,
    "My new asset",
    "My asset description"
)
