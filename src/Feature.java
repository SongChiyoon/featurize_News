import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Created by songchiyun on 2017. 4. 12..
 */
public class Feature implements Comparable<Feature>{

    double weight;
    int index;
    int newIndex;


    Feature(double w, int i){
        this.newIndex = -1;
        this.weight = w;
        this.index = i;
    }
    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {

        this.weight = weight;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public int getNewIndex() {
        return newIndex;
    }

    public void setNewIndex(int newIndex) {
        this.newIndex = newIndex;
    }

    @Override
    public int compareTo(Feature f) {
        return -Double.compare(getWeight(), f.getWeight());
        /*if (newIndex != -1)
            return -Double.compare(getWeight(), f.getWeight());
        else {
            if (this.getWeight() != f.getWeight())
                return -Double.compare(getWeight(), f.getWeight());
            else {
                return Integer.compare(this.newIndex, f.getNewIndex());
            }
        }*/
    }
}
