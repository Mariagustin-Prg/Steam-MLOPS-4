import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df_PlayTimeGenre = pd.read_csv("./data/data_to_functions/PlayTimeGenre.csv")

@app.get("/functions/PlayTime/{genero}")
def tiempo_por_juego(genero:str):
    '''
    The function wait a parameter like a: Action, Casual, Indie, Simulation, Strategy, 
    Free to Play, RPG, Sports, Adventure, Racing, Early Access, Massively Multiplayer, Animation &amp; Modeling, Video Production, Utilities, Web Publishing, Education, Software Training, Design &amp; Illustration, Audio Production, Photo Editing or Accounting.
    
    This function takes the requested genre as a parameter and returns 
    a dictionary with the year with the most played hours and the quantity of hours.
    '''
    
    row = df_PlayTimeGenre[df_PlayTimeGenre['genero']==genero].T
    list_genres = list(df_PlayTimeGenre['genero'].values)

    max_anio = 0
    for año, item in row.iterrows():
        try:    
            if item.values[0] > max_anio:
                max_anio = año
                max_playtime = item.values[0]
            return {
                f"Año de lanzamiento con más horas para género {genero}": max_anio,
                f"Cantidad de horas jugadas": max_playtime
            }
        except TypeError:
            pass
        except IndexError:
            return {"IndexError": None}
        


df_UserForGenre = pd.read_json("./data/data_to_functions/UserForGenre.json")

@app.get("/functions/UserForGenre/{genero}")
def usuarios_por_genero(genero:str):
    '''
    The function wait a parameter like a: Action, Casual, Indie, Simulation, Strategy, 
    Free to Play, RPG, Sports, Adventure, Racing, Early Access, 
    Massively Multiplayer, Animation &amp; Modeling, Video Production, Utilities, 
    Web Publishing, Education, Software Training, Design &amp; Illustration, 
    Audio Production, Photo Editing or Accounting.

    This function takes the genre as an input parameter and returns the user 
    with the most hours invested in games of that genre, as well as the 
    distribution of game hours by year.
    '''
    try:
        row = df_UserForGenre[['user', f'{genero}']]

        row = row[row[f'{genero}'].notnull()]

        return {
            f"Usuario con más horas jugadas para el género {genero}": row['user'].iloc[0],
            "Horas jugadas": row[f'{genero}'].iloc[0]
        }
    except (IndexError, KeyError):
        return {"NameError": 'The function wait a name of genre in the dataframe. Also: Action, Casual, Indie, Simulation, Strategy, Free to Play, RPG, Sports, Adventure, Racing, Early Access, Massively Multiplayer, Animation &amp; Modeling, Video Production, Utilities, Web Publishing, Education, Software Training, Design &amp; Illustration, Audio Production, Photo Editing.'}


df_UserRecommend = pd.read_json("./data/data_to_functions/UserRecommend.json")

@app.get("/functions/UserRecommend/{year}")
def recomendaciones_de_usuarios(year:int):
    '''
    The function expects an input parameter 'year' 
    containing the year for which you want to retrieve information.

    The function takes a specific year and returns the games most 
    recommended by users for the queried year.
    '''
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
        return {"Error": f"The function did not find recommendations for {year}."}


df_UserNotRecommend = pd.read_json("./data/data_to_functions/UserNotRecommend.json")

@app.get("/functions/UserNotRecommend/{year}")
def no_recomendadas_por_usuarios(year:int):
    '''
    The function expects an input parameter 'year' 
    containing the year for which you want to retrieve information.

    The function takes a specific year as an input parameter and 
    returns the games with the highest number of negative reviews.
    '''
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
        return {"Error": f"The function did not find recommendations for {year}."}



df_sentiment_analyisis = pd.read_csv("./data/data_to_functions/sentiment_analysis.csv")

@app.get("/functions/sentiment_analysis/{year}")
def analisis_de_sentimiento(year:int):
    '''
    The function expects an input parameter 'year' 
    containing the year for which you want to retrieve information.

    The function receives the requested year and returns a list of user sentiments in 
    the reviews published that year on the scale of 'Positive,' 'Neutral,' and 'Negative'.
    '''
    if not isinstance(year, int):
        raise TypeError("The function wait a integer.")            

    try:
        year = str(year)
        sentiments = list(df_sentiment_analyisis['Sentiment'].values)
        values = list(df_sentiment_analyisis[f"{year}"].values)

        return {
            f"{sentiments[0]}": int(values[0]),
            f"{sentiments[1]}": int(values[1]),
            f"{sentiments[2]}": int(values[2])
        }

    except KeyError:
        return {"Error": f"The function did not find recommendations for {year}."}
    except ValueError:
        return None



@app.get("/")
def inicio():
    return {"Welcome to API from": "Steam-MLOPS-4"}

