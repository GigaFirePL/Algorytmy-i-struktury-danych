import java.util.*;

public class UnifiedDemo {
    public static void main(String[] args) {
        // 1. Lista ocen
        List<Integer> grades = new ArrayList<>(
            Arrays.asList(5, 3, 8, 6, 2, 7, 4)
        );

        // 2. Średnia
        double avg = grades.stream()
                           .mapToInt(Integer::intValue)
                           .average()
                           .orElse(0.0);
        System.out.println("Average: " + avg);

        // 3. Filtrowanie <4
        grades.removeIf(g -> g < 4);
        // grades: [5,8,6,7,4]

        // 4. Odwróć kolejność
        Collections.reverse(grades);
        // grades: [4,7,6,8,5]

        // 5. Grupowanie
        Map<String, List<Integer>> cats = new HashMap<>();
        for (int g : grades) {
            String key = g < 4 ? "low"
                       : (g <= 6 ? "mid" : "high");
            cats.computeIfAbsent(key, k -> new ArrayList<>())
                .add(g);
        }

        // 6. Wypisz
        cats.forEach((k, vs) ->
            System.out.println(k + ": " + vs)
        );
    }
}
