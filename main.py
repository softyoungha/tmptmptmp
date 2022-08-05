from fastapi import FastAPI
from pydantic import BaseModel
from utils.tool import df_from_query, execute_sql

app = FastAPI(debug=True,
              title='my fastapi',
              description='제가 만든 API입니다')


@app.get('/')
def index():
    return {'detail': '안녕'}


@app.get('/user')
def list_all_user():
    df = df_from_query('select * from user_list')
    return {
        'data': df.to_dict(orient='records')
    }


class User(BaseModel):
    user_id: str
    user_name: str
    age: int


@app.post('/user')
def create_user(data: User):
    query = f"""
    INSERT INTO user_list   (`user_id`, `user_name`, `age`)
    VALUES                  ('{data.user_id}', '{data.user_name}', {data.age})
    """
    execute_sql(query)
    return {
        'detail': 'Succefully created'
    }


class UpdateUser(BaseModel):
    user_name: str
    age: int


@app.put('/user/{user_id}')
def update_user(user_id: str, data: UpdateUser):
    query = f"""
    UPDATE      user_list
    SET         user_name = '{data.user_name}', age = '{data.age}'
    WHERE       user_id = '{user_id}'
    """
    execute_sql(query)
    return {'detail': 'Successfully updated'}


@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    query = f"""
    DELETE FROM user_list
    WHERE       user_id = '{user_id}'
    """
    execute_sql(query)
    return {'detail': 'Successfully deleted'}
