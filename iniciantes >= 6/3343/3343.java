import java.util.*;
import java.io.IOException;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int NumT = scanner.nextInt();
        int TamM = scanner.nextInt();
        scanner.nextLine();
        String sequencia = scanner.nextLine();
        int P = scanner.nextInt();
        int M = scanner.nextInt();
        int G = scanner.nextInt();
      
        List<Integer> muralha = new ArrayList<>();
        muralha.add(TamM);

        Map<Character, Integer> ultimasPosicoes = new HashMap<>();
        ultimasPosicoes.put('P', 0);
        ultimasPosicoes.put('M', 0);
        ultimasPosicoes.put('G', 0);
      
        for (int i = 0; i < NumT; i++) {
            char tipo = sequencia.charAt(i);
            int Tvid = 0;

            if (tipo == 'P') {
                Tvid = P;
            } else if (tipo == 'M') {
                Tvid = M;
            } else if (tipo == 'G') {
                Tvid = G;
            }

            int x = ultimasPosicoes.get(tipo);

            while (Tvid > muralha.get(x)) {
                x++;
                if (x == muralha.size()) {
                    muralha.add(TamM);
                }
            }

            muralha.set(x, muralha.get(x) - Tvid);
          
            ultimasPosicoes.put(tipo, x);
        }

        System.out.println(muralha.size());
        scanner.close();
    }
}
