import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Queue;

/**
 * Created by songchiyun on 2017. 4. 12..
 */
public class Maptable {


    private int count;
    HashMap<String, Integer> map = new HashMap<>();
    HashMap<Integer, String> ItoSmap = new HashMap<>();
    private int[][] table = new int[8][10000000];
    private int index;
    Maptable(){
        index = 0;
    }

    public HashMap<Integer, String> getItoSmap() {
        return ItoSmap;
    }

    public void setItoSmap(HashMap<Integer, String> itoSmap) {
        ItoSmap = itoSmap;
    }

    public void addCount(int category, String feature){

        int position = getIndex(feature);
        if(position == index){

            table[category][position] = 1;
            map.put(feature, position);
            ItoSmap.put(position,feature);
            index++;

        }
        else{
            table[category][position]++;

        }

    }
    private int getIndex(String feature){

        if(map.containsKey(feature)){
            return map.get(feature);
        }
        else{
            return index;
        }
    }

    public int[][] getTable(){
        return this.table;
    }
    public HashMap<String, Integer> getMap(){
        return map;
    }
    public int getIndex(){
        return index;
    }

    public List<String> getSplit(String text){

        String[] feature = text.split(" ");
        List<String> splitList = new ArrayList<>();

        for(int i = 0; i < feature.length; i++){

            if(!splitList.contains(feature[i])){
                splitList.add(feature[i]);
            }
        }

        return splitList;
    }

}
