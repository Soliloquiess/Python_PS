import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[][] paper = new int[110][110];
		
		for(int p=0;p<N;p++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			for(int i=y;i<y+10;i++) {
				for(int j=x;j<x+10;j++)
					paper[i][j] = 1;
			}
		}
		int area =0;
		int length = 0;
		for(int r=1;r<=100;r++) {
			for(int c=1;c<=100;c++) {
				
			           area += paper[r][c];
			     
			}
		}
		System.out.println(area);
	}
}