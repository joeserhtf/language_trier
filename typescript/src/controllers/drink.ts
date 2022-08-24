import { Controller, Get, Post } from '@overnightjs/core';
import { Response, Request } from 'express';

export interface Drink {
    id: number;
    name: string;
    description: string;
    image: string;
    observations: string[];
    //ingredients: string;
}

let drinks: Drink[] = [
    {
        id: 1,
        name: "Margarita",
        description: "Cloyingly sweet margarita mixes have given this drink a bad name. A well-made version is a fresh mix of lime juice and tequila, with a hint of sweetener.",
        image: "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/margarita-1592951298.jpg",
        observations: [
            "light",
            "sweet",
            "fresh",
            "acid"
        ]
    },
    {
        id: 2,
        name: "Martini",
        description: "James Bond was wrong—whether you drink it with gin or vodka, stirred is the way to go when ordering a martini.",
        image: "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/martini-1592951711.jpg",
        observations: [
            "strong",
            "dry",
            "spices"
        ]
    }
];

@Controller(`drinks`)
export class DrinkController {

    @Get('')
    public async get(req: Request, res: Response): Promise<Response> {
        return res.send(drinks);
    }

    @Post('')
    public async post(req: Request, res: Response): Promise<Response> {
        //TODO validate req body
        drinks.push(req.body);
        return res.send(drinks);
    }
}