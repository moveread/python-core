export type PlayerMeta = {
    end_correct?:   number | null;
    language?:      Language | null;
    manual_labels?: { [key: string]: string } | null;
    styles?:        null | StylesNA;
    [property: string]: any;
}

export type Language = "CA" | "EN" | "DE" | "RU" | "RO" | "BG" | "FR" | "AZ" | "TR" | "PL" | "IS" | "NL" | "DK" | "N/A";

/**
 * Like `chess_notation.Styles`, but with possibly `'N/A'` annotations
 */
export type StylesNA = {
    castle?:        Castle | null;
    check?:         Check | null;
    mate?:          Mate | null;
    pawn_capture?:  PawnCapture | null;
    piece_capture?: PieceCapture | null;
    [property: string]: any;
}

export type Castle = "OO" | "O-O" | "N/A";

export type Check = "NONE" | "CHECK" | "N/A";

export type Mate = "NONE" | "SHARP" | "DOUBLE_CHECK" | "N/A";

export type PawnCapture = "de" | "dxe" | "de4" | "dxe4" | "xe4" | "PxN" | "N/A";

export type PieceCapture = "Ne4" | "Nxe4" | "NxN" | "N/A";
