package controllers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// @Summary      Get check API Response
// @Description  Responds pong
// @Tags         ping
// @Produce      json
// @Success      200
// @Router       /ping [get]
func Ping(context *gin.Context) {
	context.JSON(http.StatusOK, gin.H{"message": "pong"})
}
