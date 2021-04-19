import twint

# Configure
c = twint.Config()
c.Username = "NASA"
c.Search = "great"

# Run
twint.run.Search(c)