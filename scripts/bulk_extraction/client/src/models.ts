export type ExtractItem = {
	imageId: ImageID;
	contoured_url: string;
	annotation?: 'failed' | 'incorrect' | 'perspective-correct' | 'correct' | null;
};



export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



export type ImageID = {
	gameId: string;
	player: number;
	page: number;
	version?: number;
};



export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};

