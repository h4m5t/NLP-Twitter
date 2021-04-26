#测试代理
import twint
config = twint.Config()
config.Proxy_host = "127.0.0.1"
config.Proxy_port = 7890
config.Proxy_type = "http"

# config.User_id = "taylorswift13"

config.Username = "steve_hanke"

#config.Custom["tweet"] = ["id", "username"]
config.Output = "tweets.csv"
config.Store_csv = True

twint.run.Search(config)

