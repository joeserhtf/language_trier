package routes

import (
	"go/controllers"
	"go/middlewares"

	"github.com/gin-gonic/gin"
)

func SetupRoutes() *gin.Engine {
	router := gin.Default()
	// v1 := router.Group("/v1")
	// {
	// 	v1.GET("/ping", controllers.Ping)
	// }
	router.GET("/ping2", controllers.Ping)
	router.POST("/login", controllers.Login)
	router.POST("/signup", controllers.SignUp)
	secured := router.Group("/").Use(middlewares.Auth())
	{
		secured.GET("/ping", controllers.Ping)
	}
	return router
}
