import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { ExtractItem,ImageID } from './models';

export type DefaultData = {
        Annotate: {
                    annotation: 'failed' | 'incorrect' | 'perspective-correct' | 'correct' | "null"
requestBody: ImageID
                    
                };
    }

export class DefaultService {

	/**
	 * Get Items
	 * @returns ExtractItem Successful Response
	 * @throws ApiError
	 */
	public static getItems(): CancelablePromise<Array<ExtractItem>> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/items',
		});
	}

	/**
	 * Annotate
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static annotate(data: DefaultData['Annotate']): CancelablePromise<unknown> {
		const {
annotation,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/annotate',
			query: {
				annotation
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

}