package model

type Parameter struct{
	Name        string       `json:"name"`
	Placeholder string       `json:"placeholder"`
}

type Language struct{
	Name        string        `json:"name"`
	Extension   string        `json:"extension"`
	FileContent string        `json:"file_content"`
}

type Challenge struct {
	Name               string       `json:"name"`
	Points             uint         `json:"points"`
	Description        string       `json:"description"`
	ResolvedConclusion string       `json:"resolved_conclusion,omitempty"`
	Parameters         []Parameter  `json:"parameters"`
	Languages          []Language   `json:"languages"`
	ChallengeId        string       `json:"challenge_id"`
} 

type Challenges []Challenge
