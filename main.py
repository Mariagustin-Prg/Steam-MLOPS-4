import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df_PlayTimeGenre = pd.read_csv("./data/data_to_functions/PlayTimeGenre.csv")

@app.get("/functions/PlayTime/{genero}")
def tiempo_por_juego(genero:str):
    row = df_PlayTimeGenre[df_PlayTimeGenre['genero']==genero].T
    list_genres = list(df_PlayTimeGenre['genero'].values)

    max_anio = 0
    for año, item in row.iterrows():
        try:    
            if item.values[0] > max_anio:
                max_anio = año
                max_playtime = item.values[0]
        except TypeError:
            return {NameError: f"The function wait a name of genre in the dataframe. Also: {', '.join(list_genres)}."}
        except IndexError:
            return {NameError: f"The function wait a name of genre in the dataframe. Also: {', '.join(list_genres)}."}
    return {
        f"Año de lanzamiento con más horas para género {genero}": max_anio,
        f"Cantidad de horas jugadas en {max_anio}": max_playtime
    }

df_UserForGenre = pd.read_json("./data/data_to_functions/UserForGenre.json")

@app.get("/functions/UserForGenre/{genero}")
def usuarios_por_genero(genero:str):
    try:
        row = df_UserForGenre[['user', f'{genero}']]

        row = row[row[f'{genero}'].notnull()]

        return {
            f"Usuario con más horas jugadas para el género {genero}": row['user'].iloc[0],
            "Horas jugadas": row[f'{genero}'].iloc[0]
        }
    except (IndexError, KeyError):
        return {NameError: 'The function wait a name of genre in the dataframe. Also: Action, Casual, Indie, Simulation, Strategy, Free to Play, RPG, Sports, Adventure, Racing, Early Access, Massively Multiplayer, Animation &amp; Modeling, Video Production, Utilities, Web Publishing, Education, Software Training, Design &amp; Illustration, Audio Production, Photo Editing.'}


df_UserRecommend = pd.read_json("./data/data_to_functions/UserRecommend.json")

@app.get("/functions/UserRecommend/{year}")
def recomendaciones_de_usuarios(year:int):
    if not isinstance(year, int):
        raise TypeError("The function wait a integer.")

    try: 
        row = list(df_UserRecommend[year].values)

        return [
            {"Puesto 1": row[0][0]},
            {"Puesto 2": row[1][0]},
            {"Puesto 3": row[2][0]}
        ]
    except TypeError:
        return None
    except KeyError:
        return {"Error": f"The function doesn't find {year}'s recommendations."}


df_UserNotRecommend = pd.read_json("./data/data_to_functions/UserNotRecommend.json")

@app.get("/functions/UserNotRecommend/{year}")
def no_recomendadas_por_usuarios(year:int):
    if not isinstance(year, int):
        raise TypeError("The function wait a integer.")

    try:
        row = list(df_UserNotRecommend[year].values)

        not_recommend = {}
        for ix, no_game in enumerate(row):
            try:
                not_recommend[f"Puesto {ix + 1}"] = no_game[0]
            except TypeError:
                continue

        return not_recommend
    except KeyError:
        return {"Error": f"The function doesn't find {year}'s recommendations."}



df_sentiment_analyisis = pd.read_csv("./data/data_to_functions/sentiment_analysis.csv")

@app.get("/functions/sentiment_analysis/{year}")
def analisis_de_sentimiento(year:int):
    if not isinstance(year, int):
        raise TypeError("The function wait a integer.")            

    try:
        sentiments = list(df_sentiment_analyisis['Sentiment'].values)
        values = list(df_sentiment_analyisis[f"{year}"].values)

        zip_sentiments = zip(sentiments, values)

        dicc_sentiments = {}

        for sentiment, val in zip_sentiments:
            dicc_sentiments[f"{sentiment}"] = val

        return dicc_sentiments

    except KeyError:
        return {"Error": f"The function doesn't find {year}'s recommendations."}

@app.get("/")
def inicio():
    return {"Welcome to API from": "Steam-MLOPS-4"}

