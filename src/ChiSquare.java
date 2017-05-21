import java.io.FileWriter;
import java.util.HashMap;
import java.util.PriorityQueue;

/**
 * Created by songchiyun on 2017. 4. 11..
 */
public class ChiSquare {


    private int A, B, C, D;
    private int[][] table;
    private double[] chiResult;
    private int index;
    private int[] sumHor;
    private int[] sumVer;
    private int[] numberOfCat;
    int sum;
    ChiSquare(int index, int[] cat) {
        this.index = index;
        this.chiResult = new double[index];
        numberOfCat = cat;
        this.sum = 0;
    }

    public void setTable(int[][] table) {

        this.table = table;
    }

    private void setSum() {

        this.sumVer = new int[8];
        this.sumHor = new int[index];

        for (int c = 0; c < 8; c++) {
            sum += numberOfCat[c];
            for (int i = 1; i < index; i++) {

                sumVer[c] += table[c][i];
                sumHor[i] += table[c][i];
            }
        }

    }

    public PriorityQueue<Feature> getChiResult() {
        try {
            setSum();

            double N = 15978;
            FileWriter fw = new FileWriter("chi.txt", true);


            double[] result = new double[index];


            for (int i = 1; i < index; i++) {

                result[i] = Double.MIN_VALUE;

                for (int c = 0; c < 8; c++) {


                    A = table[c][i];
                    B = numberOfCat[c] - A;

                    C = sumHor[i] - A;
                    D = sum - (A+B+C);
                    if(A < 0 || B < 0 || C < 0 || D < 0)
                        System.out.println(A + "," + B + "," + C + "," + D);

                    fw.write(A + "," + B + "," + C + "," + D+"\n\n");
                    fw.flush();
                    double[] k = new double[4];
                    k[0] = A;
                    k[1] = B;
                    k[2] = C;
                    k[3] = D;
                    double chi = (N * Math.pow((A * D - C * B), 2)) / ((k[0]+k[2])*(k[1]+k[3])*(k[0]+k[1])*(k[2]+k[3]));
                //    double chi = (N * Math.pow((A * D - C * B), 2)) / ((A + C) * (B + D) * (A + B) * (C + D));


                    /*if(chi < 0.001){
                        chi = 0;
                    }*/
                    chi = Double.parseDouble(String.format("%.3f",chi));
                    if (result[i] < chi)
                        result[i] = chi;

                }
            }

            PriorityQueue<Feature> flist = new PriorityQueue<>();
            for (int i = 1; i < index; i++) {
                if(result[i] < 0.001) {
                    System.out.println(result[i]);
                    result[i] = 0;
                }
                Feature f = new Feature(result[i], i);
                flist.add(f);
            }
            return flist;
        }catch(Exception e){}return null;
    }

}





