import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { Body_create_game,Either_DBError_Game_,Either_DBError_NoneType_,Either_DBError_str_,Either_Union_DBError__InvalidData__InexistentItem__Game_,Game_Input,Body_Add_modify_Image,Body_annotate_image,Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InexistentImage__InvalidData__DBError__Game_,Either_Union_InexistentSchema__InvalidData__InexistentGame__InexistentPlayer__InexistentSheet__InexistentImage__DBError__Game_,Body_extract,Either_Union_NotEnoughRows__NotEnoughCols__Result_ } from './models';

export type GamesData = {
        ListGames: {
                    batchSize?: number | null
                    
                };
ReadGame: {
                    id: string
                    
                };
CreateGame: {
                    black?: Array<Blob | File> | null
formData: Body_create_game
id: string
                    
                };
UpsertGame: {
                    id: string
requestBody: Game_Input
                    
                };
    }

export type ImagesData = {
        AddModifyImage: {
                    formData: Body_Add_modify_Image
gameId: string
page: number
player: number
version?: number | null
                    
                };
AnnotateImage: {
                    formData: Body_annotate_image
gameId: string
page: number
player: number
schema: string
version: number
                    
                };
    }

export type OpsData = {
        Extract: {
                    descaleHeight?: number | null
formData: Body_extract
model: 'fcde' | 'llobregat23'
                    
                };
    }

export type DefaultData = {
        
    }

export class GamesService {

	/**
	 * List Games
	 * @returns Either_DBError_str_ Successful Response
	 * @throws ApiError
	 */
	public static listGames(data: GamesData['ListGames'] = {}): CancelablePromise<Array<Either_DBError_str_>> {
		const {
batchSize,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/games/all',
			query: {
				batch_size: batchSize
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Game
	 * @returns Either_Union_DBError__InvalidData__InexistentItem__Game_ Successful Response
	 * @throws ApiError
	 */
	public static readGame(data: GamesData['ReadGame']): CancelablePromise<Either_Union_DBError__InvalidData__InexistentItem__Game_> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/games/',
			query: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Game
	 * @returns Either_DBError_Game_ Successful Response
	 * @throws ApiError
	 */
	public static createGame(data: GamesData['CreateGame']): CancelablePromise<Either_DBError_Game_> {
		const {
id,
formData,
black,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/games/',
			query: {
				id, black
			},
			formData: formData,
			mediaType: 'multipart/form-data',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Upsert Game
	 * @returns Either_DBError_NoneType_ Successful Response
	 * @throws ApiError
	 */
	public static upsertGame(data: GamesData['UpsertGame']): CancelablePromise<Either_DBError_NoneType_> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/games/',
			query: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export class ImagesService {

	/**
	 * Add/Modify Image
	 * @returns Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InexistentImage__InvalidData__DBError__Game_ Successful Response
	 * @throws ApiError
	 */
	public static addModifyImage(data: ImagesData['AddModifyImage']): CancelablePromise<Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InexistentImage__InvalidData__DBError__Game_> {
		const {
gameId,
player,
page,
formData,
version,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/images/',
			query: {
				gameId, player, page, version
			},
			formData: formData,
			mediaType: 'multipart/form-data',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Annotate Image
	 * @returns Either_Union_InexistentSchema__InvalidData__InexistentGame__InexistentPlayer__InexistentSheet__InexistentImage__DBError__Game_ Successful Response
	 * @throws ApiError
	 */
	public static annotateImage(data: ImagesData['AnnotateImage']): CancelablePromise<Either_Union_InexistentSchema__InvalidData__InexistentGame__InexistentPlayer__InexistentSheet__InexistentImage__DBError__Game_> {
		const {
gameId,
player,
page,
version,
schema,
formData,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/images/annotate',
			query: {
				gameId, player, page, version, schema
			},
			formData: formData,
			mediaType: 'multipart/form-data',
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export class OpsService {

	/**
	 * Extract
	 * @returns Either_Union_NotEnoughRows__NotEnoughCols__Result_ Successful Response
	 * @throws ApiError
	 */
	public static extract(data: OpsData['Extract']): CancelablePromise<Either_Union_NotEnoughRows__NotEnoughCols__Result_> {
		const {
model,
formData,
descaleHeight,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/extract/',
			query: {
				model, descale_height: descaleHeight
			},
			formData: formData,
			mediaType: 'multipart/form-data',
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export class DefaultService {

	/**
	 * Ping
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static ping(): CancelablePromise<unknown> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/',
		});
	}

}