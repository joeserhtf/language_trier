package main

import (
	"go/database"
	"go/routes"

	_ "go/docs"

	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

// @title     Trying Go API
func main() {
	// Initialize Database
	database.Connect("root@tcp(localhost:3306)/language_trier?parseTime=true")
	database.Migrate()

	// Initialize Router
	router := routes.SetupRoutes()

	//Setup Swagger
	router.GET("/docs/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))

	router.Run("127.0.0.1:8000")
}
