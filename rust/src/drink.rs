use std::sync::Mutex;

use actix_web::{
    get,
    http::header::ContentType,
    post,
    web::{Data, Json},
    HttpResponse,
};
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize)]
pub struct Drink {
    pub id: i32,
    pub name: String,
    pub description: String,
    pub image: String,
    //pub observations: Vec<String>,
}

#[get("/drinks")]
pub async fn list(drinks: Data<Mutex<Vec<Drink>>>) -> HttpResponse {
    // TODO find the last 50 tweets and return them

    HttpResponse::Ok()
        .content_type(ContentType::json())
        .json(drinks)
}

#[post("/drinks")]
pub async fn insert(drinks: Data<Mutex<Vec<Drink>>>, drink: Json<Drink>) -> HttpResponse {
    let mut my_data = drinks.lock().unwrap();

    my_data.push(Drink {
        id: drink.id,
        name: drink.name.to_string(),
        description: drink.description.to_string(),
        image: drink.image.to_string(),
        // observations: [
        //     "light".to_string(),
        //     "sweet".to_string(),
        //     "fresh".to_string(),
        //     "acid".to_string(),
        // ].to_vec()
    });

    HttpResponse::Ok()
        .content_type(ContentType::json())
        .json(&*my_data)
}
