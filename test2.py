# 测试twint
import twint

# Configure
c = twint.Config()
c.Username = "nasa"
c.Search = "great"

# Run
twint.run.Search(c)