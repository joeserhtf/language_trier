package models

type Drink struct {
	Id           int      `json:"id" form:"id" binding:"required"`
	Name         string   `json:"name" form:"name" binding:"required"`
	Description  string   `json:"description" form:"description" binding:"required"`
	Image        string   `json:"image" form:"image" binding:"required"`
	Observations []string `json:"observations" form:"observations" binding:"required"`
}
