use std::sync::Mutex;

use actix_web::{
    get,
    web::{self, Data},
    Responder, Result,
};
use serde::Serialize;

use crate::drink::Drink;

mod drink;

#[derive(Serialize)]
struct BasicObj {
    message: String,
}

#[get("/ping")]
async fn index() -> Result<impl Responder> {
    let obj = BasicObj {
        message: "pong".to_string(),
    };
    Ok(web::Json(obj))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    use actix_web::{App, HttpServer};

    let drinks: Vec<Drink> = vec![
        Drink {
            id: 1,
            name: "Margarita".to_string(), 
            description: "Cloyingly sweet margarita mixes have given this drink a bad name. A well-made version is a fresh mix of lime juice and tequila, with a hint of sweetener.".to_string(),
            image: "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/margarita-1592951298.jpg".to_string(),
            // observations: [
            //     "light".to_string(),
            //     "sweet".to_string(),
            //     "fresh".to_string(),
            //     "acid".to_string(),
            // ].to_vec()
        },
        Drink {
            id: 2,
            name: "Martini".to_string(), 
            description: "James Bond was wrong—whether you drink it with gin or vodka, stirred is the way to go when ordering a martini.".to_string(),
            image: "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/martini-1592951711.jpg".to_string(),
            // observations: [
            //     "strong".to_string(),
            //     "dry".to_string(),
            //     "spices".to_string(),
            // ].to_vec()
        },
    ];

    let data = Data::new(Mutex::new(drinks));

    HttpServer::new(move || {
        App::new()
            .app_data(Data::clone(&data))
            .service(index)
            .service(drink::list)
            .service(drink::insert)
    })
    .bind(("127.0.0.1", 8000))?
    .run()
    .await
}
