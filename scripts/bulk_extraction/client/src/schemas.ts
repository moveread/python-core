export const $ExtractItem = {
	properties: {
		imageId: {
	type: 'ImageID',
	isRequired: true,
},
		contoured_url: {
	type: 'string',
	isRequired: true,
},
		annotation: {
	type: 'any-of',
	contains: [{
	type: 'Enum',
	enum: ['failed','incorrect','perspective-correct','correct',],
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