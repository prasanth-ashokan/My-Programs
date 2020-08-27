import { AbstractControl, ValidationErrors } from '@angular/forms';

export class UsernameValidators {
    
    static cannotContainSpaceSymbol(control: AbstractControl): ValidationErrors | null {
        if ((control.value as string).indexOf(' ') != -1) {
       return {
           cannotContainSpaceSymbol:true
       }
        }
        const l=['1','2','3','4','5','6','7','8','9','0', '#','!','~',"@","$","%","^","&","*","?"]
        for(let i of l){

        if ((control.value as string).indexOf(i) != -1) {
            return {
                cannotContainSpaceSymbol:true
            }
             }
            }
        return null;
}
}
