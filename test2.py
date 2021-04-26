# 爬虫主体
import twint

# Configure
c = twint.Config()
c.Username = "nasa"
c.Search = "great"

# Run
twint.run.Search(c)