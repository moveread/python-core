export type Body_Add_Image = {
	img: Blob | File;
};



export type Body_Modify_image = {
	img: Blob | File;
};



export type Body_create_game = {
	/**
	 * White's images
	 */
	white: Array<Blob | File>;
};



export type Box = {
	url: string;
	meta?: Record<string, unknown> | null;
};



export type DBError = {
	detail?: unknown;
	reason?: "db-error";
};



export type Either_DBError_Game_ = {
	value: DBError | Game_Output;
	tag: 'left' | 'right';
};




export type Either_DBError_NoneType_ = {
	value: DBError | null;
	tag: 'left' | 'right';
};




export type Either_DBError_str_ = {
	value: DBError | string;
	tag: 'left' | 'right';
};




export type Either_Union_DBError__InvalidData__InexistentItem__Game_ = {
	value: DBError | InvalidData | InexistentItem | Game_Output;
	tag: 'left' | 'right';
};




export type Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InvalidData__DBError__Game_ = {
	value: InexistentGame | InexistentSheet | InexistentPlayer | InvalidData | DBError | Game_Output;
	tag: 'left' | 'right';
};




export type Game_Input = {
	id: string;
	players: Array<Player_Input>;
	meta?: Record<string, unknown> | null;
};



export type Game_Output = {
	id: string;
	players: Array<Player_Output>;
	meta?: Record<string, unknown> | null;
};



export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



export type Image = {
	url: string;
	boxes?: Array<Box> | null;
	meta?: Record<string, unknown> | null;
};



export type InexistentGame = {
	gameId: string;
	detail?: unknown;
	reason?: "inexistent-game";
};



export type InexistentItem = {
	key: string;
	detail?: unknown | null;
	reason?: "inexistent-item";
};



export type InexistentPlayer = {
	playerId: PlayerID;
	num_players: number;
	detail?: unknown;
	reason?: "inexistent-player";
};



export type InexistentSheet = {
	sheetId: SheetID;
	num_pages: number;
	detail?: unknown;
	reason?: "inexistent-sheet";
};



export type InvalidData = {
	detail?: unknown;
	reason?: "invalid-data";
};



export type Player_Input = {
	sheets: Array<Sheet_Input>;
	meta?: Record<string, unknown> | null;
};



export type Player_Output = {
	sheets: Array<Sheet_Output>;
	meta?: Record<string, unknown> | null;
};



export type PlayerID = {
	gameId: string;
	player: number;
};



export type Sheet_Input = {
	images: Array<Image>;
	meta?: Record<string, unknown> | null;
};



export type Sheet_Output = {
	images: Array<Image>;
	meta?: Record<string, unknown> | null;
};



export type SheetID = {
	gameId: string;
	player: number;
	page: number;
};



export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};

