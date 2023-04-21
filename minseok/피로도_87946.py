def DFS(k,dungeons,visited,cnt):
    global answer
    answer = max(cnt,answer)         # 현재 cnt값을 answer에 저장
    for i in range(len(dungeons)):
        if visited[i]==0 and dungeons[i][0]<=k:
            visited[i]=1             # 현재 노드 방문처리
            DFS(k-dungeons[i][1],dungeons,visited,cnt+1)  # 현재 피로도에서 소모 피로도를 빼고 cnt+1을 한 후 DFS  
            visited[i]=0             # 더 방문할 노드가 없다면 방문 처리 해제           
        
def solution(k, dungeons):
    global answer
    visited = [0]*len(dungeons)     # 방문처리할 리스트 생성
    
    DFS(k,dungeons,visited,0)       
    return answer
answer = 0
