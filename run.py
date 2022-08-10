from shop import route, app

app.config["SECRET_KEY"] = "sid00100"



if __name__=="__main__":
  app.run(debug=True)
    