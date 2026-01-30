import gazu

gazu.set_host("http://localhost/api")
gazu.set_event_host("http://localhost/api")
user = gazu.log_in("admin@example.com", "mysecretpassword")

def my_callback(data):
    print("Asset created %s" % data["asset_id"])

event_client = gazu.events.init()
gazu.events.add_listener(event_client, "asset:new", my_callback)
gazu.events.run_client(event_client)
