

import java.util.Date;
import java.util.Locale;


public class Main {


    public static void main(String[] args) {
        Date relogio = new Date();
        System.out.printf("Hora em tempo real: ");
        System.out.println(relogio.toString());
        Locale indioma =  Locale.getDefault();
        System.out.println("indioma local: " + indioma.getDisplayLanguage());
        System.out.println("Localizaçao: " + indioma.getDisplayCountry());



        }
    }
