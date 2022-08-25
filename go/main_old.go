package main

import (
	"net/http"

	"go/models"

	"github.com/gin-gonic/gin"
)

var drinks = []models.Drink{
	{
		Id:          1,
		Name:        "Margarita",
		Description: "Cloyingly sweet margarita mixes have given this drink a bad name. A well-made version is a fresh mix of lime juice and tequila, with a hint of sweetener.",
		Image:       "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/margarita-1592951298.jpg",
		Observations: []string{
			"light",
			"sweet",
			"fresh",
			"acid",
		},
	},
	{
		Id:          2,
		Name:        "Martini",
		Description: "James Bond was wrong—whether you drink it with gin or vodka, stirred is the way to go when ordering a martini.",
		Image:       "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/martini-1592951711.jpg",
		Observations: []string{
			"strong",
			"dry",
			"spices",
		},
	},
}

func main() {
	router := gin.Default()
	router.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})

	router.GET("/drinks", func(c *gin.Context) {
		c.JSON(http.StatusOK, drinks)
	})

	router.POST("/drinks", func(c *gin.Context) {
		//TODO not need validate
		var json models.Drink

		if err := c.ShouldBindJSON(&json); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		drinks = append(drinks, json)

		c.JSON(http.StatusOK, drinks)
	})

	router.Run("127.0.0.1:8000")
}
