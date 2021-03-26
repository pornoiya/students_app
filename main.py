from web.view import app, db
from config import config

# Почему фласк? В университете все веб приложения я писала на фласке. Я уже знакома с этим
# фреймворком, поэтому выбрала его.
# Почему postgres? Я умею работать с постгресом через psql, это полезно когда база на удаленном
# сервере.

if __name__ == "__main__":
    app.run(debug=config.APP_DEBUG,
            host=config.APP_HOST, port=config.APP_PORT)
    db.conn.close()
