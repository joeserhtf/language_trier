import { Controller, Get } from '@overnightjs/core';
import { Response, Request } from 'express';

@Controller(`ping`)
export class PingController {

    @Get('')
    public async get(req: Request, res: Response): Promise<Response> {
        return res.send({
            message: "pong"
        });
    }
}