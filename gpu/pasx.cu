/* Created by Language version: 7.1.0 cacheloop */
/* VECTORIZED */
#include <stdio.h>
#include <math.h>
#include "scoplib.h"
#undef PI
#define nil 0
 
#include "md1redef.h"
#include "section.h"
#include "md2redef.h"

#if METHOD3
extern int _method3;
#endif

#include "nrncuda.h"

#undef exp
#define exp hoc_Exp
extern double hoc_Exp();
 
#if !defined(CACHELOOP)
#define CACHELOOP GPU_PODSIZE 
#endif
#if CACHELOOP
#define _cldec int _clj;
#define _cldecjj int _cljj=0, _clss=1;
#define _cldec0 int _clj = 0;
#define _cls CACHELOOP
#define _cloff * _cls + _clj
#define _cljarg _clj,
#define _cljproto int _clj,
#define _clb for (_clj = 0; _clj < _cls; ++_clj) {
#define _cle }
#else
 
#undef CACHELOOP
#define CACHELOOP 0
#define _cldec /**/
#define _cldecjj /**/
#define _cldec0 /**/
#define _cloff /**/
#define _cljarg /**/
#define _cljproto /**/
#define _clj 0
#define _cls 1
#define _cljj 0
#define _clss 1
#define _clb /**/
#define _cle /**/
#endif
 

typedef void(*Pvmi)(_NrnThread* _nt, _Memb_list* _ml, int); 

#define _threadargscomma_ _p, _ppvar, _cljarg _thread, _nt,
#define _threadargs_ _p, _ppvar, _cljarg _thread, _nt
 
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, _cljproto Datum* _thread, _NrnThread* _nt,
#define _threadargsproto_ double* _p, Datum* _ppvar, _cljproto Datum* _thread, _NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define g _p[0 _cloff]
#define e _p[1 _cloff]
#define i _p[2 _cloff]
#define v _p[3 _cloff]
#define _g _p[4 _cloff]
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif

extern "C" {
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 /* declaration of user functions */
 extern int ret(double);
 static int _mechtype;

extern int nrn_get_mechtype(const char*);
extern void _nrn_cacheloop_reg(int type, int cls);
extern void hoc_register_prop_size(int type, int _psize, int _dsize);
extern void hoc_register_cuda_capable(int _type, int _capable);
extern void hoc_register_var(DoubScal* scdoub, DoubVec* vdoub, IntFunc* function);
extern void ivoc_help(char* p);
extern void hoc_register_limits(int type, HocParmLimits* limits);
extern void hoc_register_units( int type, HocParmUnits* units);
extern Memb_func* memb_func;


static int _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
 _extcall_prop = _prop;
 ret(1.);
 return 1;
}
 /* connect user functions to hoc names */
 static IntFunc hoc_intfunc[] = {
 "setdata_pasx", _hoc_setdata,
 0, 0
};
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 "g_pasx", 0, 1e+09,
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "g_pasx", "S/cm2",
 "e_pasx", "mV",
 "i_pasx", "mA/cm2",
 0,0
};
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop* _prop);
 static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) ;
 static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) ;
 static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) ;
 static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type) ;
 /* connect range variables in _p that hoc is supposed to know about */
 static char *_mechanism[] = {
 "7.2.0 nrncuda",
"pasx",
 "g_pasx",
 "e_pasx",
 0,
 "i_pasx",
 0,
 0,
 0};

#define atomicAdd _pasx_atomicAdd
__device__ double _pasx_atomicAdd(double* address, double val)
{
    double old = *address, assumed;
    do {
        assumed = old;
        old =
           __longlong_as_double(
                  atomicCAS((unsigned long long int*)address,
                            __double_as_longlong(assumed),
                            __double_as_longlong(assumed + val)));
    } while (assumed != old);
    return old;
}

static void nrn_alloc(Prop* _prop)
{
	Prop *prop_ion, *need_memb(), *need_memb_cl();
	double *_p; Datum *_ppvar;
 	_cldec0 _cldecjj
 
#if CACHELOOP
	_p = nrn_prop_data_alloc_cl(_mechtype, 5, _prop, &_clj, &_ppvar, 0);
#else
 	_p = nrn_prop_data_alloc(_mechtype, 5, _prop);
 
#endif
 	/*initialize range parameters*/
 	g = 0.001;
 	e = -70;
 	_prop->param = _p;
 	_prop->param_size = 5;

	//printf("Done with nrn_alloc in pasx.cu\n");

}

extern void register_mech(char**, void(*)(Prop*), Pvmi, Pvmi, Pvmi, Pvmi, int, int);
static void _initlists();
void _pasx_reg() {
	int _vectorized = 1;
  _initlists();
 	register_mech(_mechanism, nrn_alloc, nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 1);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
 _nrn_cacheloop_reg(_mechtype, _cls);
  hoc_register_prop_size(_mechtype, 5, 0);
  hoc_register_cuda_capable(_mechtype, 1);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 pasx ./pasx.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }

static int _reset;
static char *modelname = "passive membrane channel";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}

static void initmodel(_threadargsproto_) {
  int _i; double _save;{
}
}

/*
static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread; _cldec
Node *_nd; int* _ni; int _iml, _cntml;
    _ni = _ml->_nodeindices;
    _cntml = _ml->_nodecount;
    _thread = _ml->_thread;
    for (_iml = 0; _iml < _cntml; ++_iml) {
        _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
        _clb v = VEC_V(_ni[_iml*_cls + _clj]); _cle
        initmodel(_threadargs_);
    }
}
*/

/*
__global__ void 
_initmodel(_threadargsproto_) {
  int _i; double _save;{
}
}
*/

__global__ void
gpu_init_kernel(nrncuda_defines_t dp, nrncuda_memb_prop_t mp)
{
	double _rhs;
	Datum* _ppvar;
        _cldec

        int _pod  = (blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &dp._params[mp.param_start_offset + podoffset*5];
        int node = dp._nodeindices[mp.node_start_offset + podoffset + _clj];

        v = dp.VEC._v[node]; 
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;
        int num_blocks;
        int num;

        /* need to work out an optimal strategy for setting up the grid based on the number of
         compartments and the number of mechanisms. But for starters, we will just use
         number of nodes. */

	_ml->nrncuda_info->num_pods = _ml->_nodecount;
        num_blocks = _ml->_nodecount * GPU_PODSIZE / GPU_ADVANCE_BLOCKSIZE;
        num = num_blocks * GPU_ADVANCE_BLOCKSIZE;
        if (_ml->_nodecount * GPU_PODSIZE > num) num_blocks += 1;
	_ml->nrncuda_info->num_blocks = num_blocks;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(_ml->nrncuda_info->num_blocks, 1, 1);

        gpu_init_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, *_ml->nrncuda_info);
        err = cudaGetLastError();
 
	// printf("Done with pasx init\n");

}

//#define _threadargscomma_ _p, _ppvar, _cljarg _thread, _nt,
#define _threadargscommakern_ _p, _ppvar, _clj,
//#define _threadargsprotocomma_ double* _p, Datum* _ppvar, _cljproto Datum* _thread, _NrnThread* _nt,
#define _threadargsprotocommakern_ double* _p, Datum* _ppvar, int _clj, 
/*
__device__ void _pasx_current(_threadargsprotocommakern_ double* _current){ 
    *_current = 0.;
    i = g * ( v - e );
    *_current += i;
}
*/
#define _pasx_current(_current) \
    *_current = 0.; \
    i = g * ( v - e ); \
    *_current += i; \

__global__ void
gpu_pasx_cur_kernel(nrncuda_defines_t dp, nrncuda_memb_prop_t mp)
{
	double _rhs;
	Datum* _ppvar;
        _cldec

	double lv;
	double li;
	double lg;
	double l_rhs;
	double le;
	double l_g;

        int _pod=(blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &dp._params[mp.param_start_offset + podoffset*5];
        int node = dp._nodeindices[mp.node_start_offset + podoffset + _clj];

        lv = dp.VEC._v[node];
	lv += 0.001;

	lg = g;
	le = e;
        l_g = lg * ( lv - le );
	lv -= 0.001;
        l_rhs = lg * ( lv - le );
        _g = (l_g - l_rhs)*1000.0; 

	atomicAdd(&dp.VEC._rhs[node], -l_rhs);

/*
        v = dp.VEC._v[node];
	v += 0.001;
	_pasx_current(_threadargscommakern_ &_g);
	v -= 0.001;
	_pasx_current(_threadargscommakern_ &_rhs);
        _g = (_g - _rhs)*1000.0; 

	atomicAdd(&dp.VEC._rhs[node], -_rhs);
*/
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;
        int num_blocks;
        int num;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(_ml->nrncuda_info->num_blocks, 1, 1);

        err = cudaMemcpy( _nt->nrncuda_defines.VEC._rhs,  _nt->_actual_rhs,
                          _nt->nrncuda_defines.VEC._size_rhs, cudaMemcpyHostToDevice);
        if (err != cudaSuccess) return;
        gpu_pasx_cur_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, *_ml->nrncuda_info);
        err = cudaGetLastError();
        if (err != cudaSuccess) return;
        err = cudaMemcpy( _nt->_actual_rhs, _nt->nrncuda_defines.VEC._rhs,
                          _nt->nrncuda_defines.VEC._size_rhs, cudaMemcpyDeviceToHost);
        if (err != cudaSuccess) return;
 
	// printf("Done with pasx cur\n");

}
/*
static void _nrn_current(_threadargsprotocomma_ double* _current){ _clb _current[_clj] = 0.; _cle
{ {
   _clb i = g * ( v - e ) ;
   _cle }
 _clb _current[_clj] += i; _cle
}}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread; _cldec0
Node *_nd; int* _ni; double _rhs[_cls]; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _clb v = VEC_V(_ni[_iml*_cls + _clj]); _cle
 _clb v += .001; _cle;
 {_cldec0 _nrn_current(_threadargscomma_ &_g);}
 _clb v -= .001; _cle;
{ {_cldec0 _nrn_current(_threadargscomma_ _rhs);}
 	}
 _clb _g = (_g - _rhs[_clj])/.001; _cle
 _clb VEC_RHS(_ni[_iml*_cls + _clj]) -= _rhs[_clj]; _cle
  printf("Done with nrn_cur in pasx.cu\n");
 
}}
*/

__global__ void
gpu_pasx_jacob_kernel(nrncuda_defines_t dp, nrncuda_memb_prop_t mp)
{
	double _rhs;
	Datum* _ppvar;
        _cldec

        int _pod  = (blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &dp._params[mp.param_start_offset + podoffset*5];
        int node = dp._nodeindices[mp.node_start_offset + podoffset + _clj];
        atomicAdd(&dp.VEC._d[node], _g);
}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;
        int num_blocks;
        int num;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(_ml->nrncuda_info->num_blocks, 1, 1);

        err = cudaMemcpy( _nt->nrncuda_defines.VEC._d,  _nt->_actual_d,
                          _nt->nrncuda_defines.VEC._size_d, cudaMemcpyHostToDevice);
        if (err != cudaSuccess) return;
        gpu_pasx_jacob_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, *_ml->nrncuda_info);
        err = cudaGetLastError();
        if (err != cudaSuccess) return;
        err = cudaMemcpy( _nt->_actual_d, _nt->nrncuda_defines.VEC._d,
                          _nt->nrncuda_defines.VEC._size_d, cudaMemcpyDeviceToHost);
        if (err != cudaSuccess) return;

        // printf("Done with pasx jacob\n");

}

/*
static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread; _cldec0
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	_clb VEC_D(_ni[_iml*_cls + _clj]) += _g; _cle
  }else
#endif
  {
     _clb _nd = _ml->_nodelist[_iml*_cls + _clj];
	NODED(_nd) += _g; _cle
  }
 
  printf("Done with nrn_jacob in pasx.cu\n");
}}
*/

__global__ void
gpu_pasx_state_kernel(nrncuda_defines_t dp, nrncuda_memb_prop_t mp)
{
	double _rhs;
	Datum* _ppvar;
        _cldec

        int _pod  = (blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &dp._params[mp.param_start_offset + podoffset*5];
        int node = dp._nodeindices[mp.node_start_offset + podoffset + _clj];
}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;
        int num_blocks;
        int num;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(_ml->nrncuda_info->num_blocks, 1, 1);

        gpu_pasx_state_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, *_ml->nrncuda_info);
        err = cudaGetLastError();

        // printf("Done with pasx states\n");

}

/*
static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {

  printf("Done with nrn_state in pasx.cu\n");
}
*/

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x; _cldec0
 int _i; static int _first = 1;
  if (!_first) return;
_first = 0;
}
}
