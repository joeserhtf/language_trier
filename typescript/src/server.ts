import { Server } from '@overnightjs/core';
import express, { Application } from 'express';
import { PingController } from './controllers/ping';
import * as http from "http";
import { DrinkController } from './controllers/drink';

export class SetupServer extends Server {
    private httpServer: http.Server | undefined;

    constructor(private port = 8000) {
        super();
    }

    public async init(): Promise<void> {
        this.setupExpress();
        this.setupControllers();
    }

    private setupExpress(): void {
        this.app.use(express.json({ limit: '50mb' }));
        this.app.use(express.urlencoded({ limit: '50mb', extended: true }));
    }

    private setupControllers(): void {
        const pingController = new PingController();
        const drinkController = new DrinkController();
        this.addControllers([
            pingController,
            drinkController
        ]);
    }

    public getApp(): Application {
        return this.app;
    }

    public start(): void {
        this.httpServer = this.app.listen(this.port, () => {
            console.log('Server listening on port: ' + this.port);
        });
    }
}