(******************************************************************)
(*     Restriction file for SM.fr                                 *)
(*                                                                *)                                            
(*     The CKM matrix is diagonal                                 *)
(******************************************************************)

M$Restrictions = {
            CKM[i_,i_] -> 1,
            CKM[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= j),
            cabi -> 0,
            RA[i_,i_] -> 1,
            RA[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= j),
            a1 -> 0,
            a2 -> 0,
            a3 -> 0

}
