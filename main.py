from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(body: dict = Body(...)):
    print(body)
    return {"new_post": f"title {body['title']} content: {body['content']}"}
