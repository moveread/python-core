export type GameMeta = {
    headers?:    Headers | null;
    pgn?:        null | string;
    tournament?: Tournament | null;
}

export type Headers = {
    black?:  null | string;
    date?:   null | string;
    event?:  null | string;
    result?: null | string;
    round?:  number | null;
    site?:   null | string;
    white?:  null | string;
}

export type Tournament = {
    board?: number | null;
    group?: null | string;
    name?:  null | string;
    round?: number | null;
}
