export const $Body_Add_modify_Image = {
	properties: {
		img: {
	type: 'binary',
	isRequired: true,
	format: 'binary',
},
	},
} as const;

export const $Body_annotate_image = {
	properties: {
		meta: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'array',
	contains: {
	properties: {
	},
},
}, {
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}],
	isRequired: true,
},
	},
} as const;

export const $Body_create_game = {
	properties: {
		white: {
	type: 'array',
	contains: {
	type: 'binary',
	format: 'binary',
},
	isRequired: true,
},
	},
} as const;

export const $Body_extract = {
	properties: {
		sheet: {
	type: 'binary',
	isRequired: true,
	format: 'binary',
},
	},
} as const;

export const $Box = {
	properties: {
		url: {
	type: 'string',
	isRequired: true,
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $DBError = {
	properties: {
		detail: {
	properties: {
	},
},
		reason: {
	type: '"db-error"',
},
	},
} as const;

export const $Either_DBError_Game_ = {
	properties: {
		value: {
	type: 'any-of',
	contains: [{
	type: 'DBError',
}, {
	type: 'Game_Output',
}],
	isRequired: true,
},
		tag: {
	type: 'Enum',
	enum: ['left','right',],
	isRequired: true,
},
	},
} as const;

export const $Either_DBError_NoneType_ = {
	properties: {
		value: {
	type: 'any-of',
	contains: [{
	type: 'DBError',
}, {
	type: 'null',
}],
	isRequired: true,
},
		tag: {
	type: 'Enum',
	enum: ['left','right',],
	isRequired: true,
},
	},
} as const;

export const $Either_DBError_str_ = {
	properties: {
		value: {
	type: 'any-of',
	contains: [{
	type: 'DBError',
}, {
	type: 'string',
}],
	isRequired: true,
},
		tag: {
	type: 'Enum',
	enum: ['left','right',],
	isRequired: true,
},
	},
} as const;

export const $Either_Union_DBError__InvalidData__InexistentItem__Game_ = {
	properties: {
		value: {
	type: 'any-of',
	contains: [{
	type: 'DBError',
}, {
	type: 'InvalidData',
}, {
	type: 'InexistentItem',
}, {
	type: 'Game_Output',
}],
	isRequired: true,
},
		tag: {
	type: 'Enum',
	enum: ['left','right',],
	isRequired: true,
},
	},
} as const;

export const $Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InexistentImage__InvalidData__DBError__Game_ = {
	properties: {
		value: {
	type: 'any-of',
	contains: [{
	type: 'InexistentGame',
}, {
	type: 'InexistentSheet',
}, {
	type: 'InexistentPlayer',
}, {
	type: 'InexistentImage',
}, {
	type: 'InvalidData',
}, {
	type: 'DBError',
}, {
	type: 'Game_Output',
}],
	isRequired: true,
},
		tag: {
	type: 'Enum',
	enum: ['left','right',],
	isRequired: true,
},
	},
} as const;

export const $Either_Union_InexistentSchema__InvalidData__InexistentGame__InexistentPlayer__InexistentSheet__InexistentImage__DBError__Game_ = {
	properties: {
		value: {
	type: 'any-of',
	contains: [{
	type: 'InexistentSchema',
}, {
	type: 'InvalidData',
}, {
	type: 'InexistentGame',
}, {
	type: 'InexistentPlayer',
}, {
	type: 'InexistentSheet',
}, {
	type: 'InexistentImage',
}, {
	type: 'DBError',
}, {
	type: 'Game_Output',
}],
	isRequired: true,
},
		tag: {
	type: 'Enum',
	enum: ['left','right',],
	isRequired: true,
},
	},
} as const;

export const $Either_Union_NotEnoughRows__NotEnoughCols__Result_ = {
	properties: {
		value: {
	type: 'any-of',
	contains: [{
	type: 'NotEnoughRows',
}, {
	type: 'NotEnoughCols',
}, {
	type: 'Result',
}],
	isRequired: true,
},
		tag: {
	type: 'Enum',
	enum: ['left','right',],
	isRequired: true,
},
	},
} as const;

export const $Game_Input = {
	properties: {
		id: {
	type: 'string',
	isRequired: true,
},
		players: {
	type: 'array',
	contains: {
		type: 'Player_Input',
	},
	isRequired: true,
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Game_Output = {
	properties: {
		id: {
	type: 'string',
	isRequired: true,
},
		players: {
	type: 'array',
	contains: {
		type: 'Player_Output',
	},
	isRequired: true,
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $HTTPValidationError = {
	properties: {
		detail: {
	type: 'array',
	contains: {
		type: 'ValidationError',
	},
},
	},
} as const;

export const $Image = {
	properties: {
		url: {
	type: 'string',
	isRequired: true,
},
		boxes: {
	type: 'any-of',
	contains: [{
	type: 'array',
	contains: {
		type: 'Box',
	},
}, {
	type: 'null',
}],
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $ImageID = {
	properties: {
		gameId: {
	type: 'string',
	isRequired: true,
},
		player: {
	type: 'number',
	isRequired: true,
},
		page: {
	type: 'number',
	isRequired: true,
},
		version: {
	type: 'number',
	default: 0,
},
	},
} as const;

export const $InexistentGame = {
	properties: {
		gameId: {
	type: 'string',
	isRequired: true,
},
		detail: {
	properties: {
	},
},
		reason: {
	type: '"inexistent-game"',
},
	},
} as const;

export const $InexistentImage = {
	properties: {
		imageId: {
	type: 'ImageID',
	isRequired: true,
},
		num_versions: {
	type: 'number',
	isRequired: true,
},
		detail: {
	properties: {
	},
},
		reason: {
	type: '"inexistent-image"',
},
	},
} as const;

export const $InexistentItem = {
	properties: {
		key: {
	type: 'string',
	isRequired: true,
},
		detail: {
	type: 'any-of',
	contains: [{
	properties: {
	},
}, {
	type: 'null',
}],
},
		reason: {
	type: '"inexistent-item"',
},
	},
} as const;

export const $InexistentPlayer = {
	properties: {
		playerId: {
	type: 'PlayerID',
	isRequired: true,
},
		num_players: {
	type: 'number',
	isRequired: true,
},
		detail: {
	properties: {
	},
},
		reason: {
	type: '"inexistent-player"',
},
	},
} as const;

export const $InexistentSchema = {
	properties: {
		schema: {
	type: 'string',
	isRequired: true,
},
		detail: {
	properties: {
	},
	isRequired: true,
},
		reason: {
	type: '"inexistent-schema"',
},
	},
} as const;

export const $InexistentSheet = {
	properties: {
		sheetId: {
	type: 'SheetID',
	isRequired: true,
},
		num_pages: {
	type: 'number',
	isRequired: true,
},
		detail: {
	properties: {
	},
},
		reason: {
	type: '"inexistent-sheet"',
},
	},
} as const;

export const $InvalidData = {
	properties: {
		detail: {
	properties: {
	},
},
		reason: {
	type: '"invalid-data"',
},
	},
} as const;

export const $NotEnoughCols = {
	properties: {
		detected: {
	type: 'number',
	isRequired: true,
},
		required: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $NotEnoughRows = {
	properties: {
		detected: {
	type: 'number',
	isRequired: true,
},
		required: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Player_Input = {
	properties: {
		sheets: {
	type: 'array',
	contains: {
		type: 'Sheet_Input',
	},
	isRequired: true,
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Player_Output = {
	properties: {
		sheets: {
	type: 'array',
	contains: {
		type: 'Sheet_Output',
	},
	isRequired: true,
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $PlayerID = {
	properties: {
		gameId: {
	type: 'string',
	isRequired: true,
},
		player: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Result = {
	properties: {
		contours: {
	type: 'array',
	contains: {
	type: 'array',
	contains: {
	type: 'array',
	contains: {
	type: 'array',
	contains: {
	type: 'number',
},
},
},
},
	isRequired: true,
},
		contoured_image: {
	type: 'string',
	isRequired: true,
},
		corrected_image: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Sheet_Input = {
	properties: {
		images: {
	type: 'array',
	contains: {
		type: 'Image',
	},
	isRequired: true,
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Sheet_Output = {
	properties: {
		images: {
	type: 'array',
	contains: {
		type: 'Image',
	},
	isRequired: true,
},
		meta: {
	type: 'any-of',
	contains: [{
	type: 'dictionary',
	contains: {
	properties: {
	},
},
}, {
	type: 'null',
}],
},
	},
} as const;

export const $SheetID = {
	properties: {
		gameId: {
	type: 'string',
	isRequired: true,
},
		player: {
	type: 'number',
	isRequired: true,
},
		page: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ValidationError = {
	properties: {
		loc: {
	type: 'array',
	contains: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'number',
}],
},
	isRequired: true,
},
		msg: {
	type: 'string',
	isRequired: true,
},
		type: {
	type: 'string',
	isRequired: true,
},
	},
} as const;