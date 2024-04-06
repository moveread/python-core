import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { Body_create_game,Either_DBError_Game_,Either_DBError_NoneType_,Either_DBError_str_,Either_Union_DBError__InvalidData__InexistentItem__Game_,Game_Input,Body_Add_Image,Body_Modify_image,Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InvalidData__DBError__Game_ } from './models';

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
        ModifyImage: {
                    formData: Body_Modify_image
gameId: string
page: number
player: number
version: number | null
                    
                };
AddImage: {
                    formData: Body_Add_Image
gameId: string
page: number
player: number
version?: number | null
                    
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
			url: '/games/',
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
			url: '/games/{id}',
			path: {
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
			url: '/games/{id}',
			path: {
				id
			},
			query: {
				black
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
			url: '/games/{id}',
			path: {
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
	 * Modify Image
	 * @returns Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InvalidData__DBError__Game_ Successful Response
	 * @throws ApiError
	 */
	public static modifyImage(data: ImagesData['ModifyImage']): CancelablePromise<Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InvalidData__DBError__Game_> {
		const {
gameId,
player,
page,
version,
formData,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/images/{gameId}/{player}/{page}/{version}',
			path: {
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
	 * Add Image
	 * @returns Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InvalidData__DBError__Game_ Successful Response
	 * @throws ApiError
	 */
	public static addImage(data: ImagesData['AddImage']): CancelablePromise<Either_Union_InexistentGame__InexistentSheet__InexistentPlayer__InvalidData__DBError__Game_> {
		const {
gameId,
player,
page,
formData,
version,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/images/{gameId}/{player}/{page}',
			path: {
				gameId, player, page
			},
			query: {
				version
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